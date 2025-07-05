from importlib.metadata import version

import tiktoken
print("tiktoken version:", version("tiktoken"))

import torch
print("PyTorch version:", torch.__version__)
from torch.utils.data import Dataset, DataLoader

#========================================= analyze_sample_file
def analyze_sample_file():
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
        print("Total number of character:", len(raw_text))
        print(raw_text[:99])

        
#========================================= first_usage_of_tokenizer
def first_usage_of_tokenizer():
    tokenizer = tiktoken.get_encoding("gpt2")
    text = (
        "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
        "of someunknownPlace."
    )
    integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
    print(integers)
    

#========================================= second_usage_of_tokenizer
def second_usage_of_tokenizer():
    tokenizer = tiktoken.get_encoding("gpt2")
    raw_text = ""
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    enc_text = tokenizer.encode(raw_text)
    print(len(enc_text))
    print(enc_text)
    
    # taking the 50 first tokens
    sample_size = 50 
    enc_sample = enc_text[:sample_size]
    print(f"======\nSample of length {sample_size}")
    print(enc_sample)

    # determining the size of the attention window
    context_size = 4
    x = enc_sample[:context_size]
    offset = 1

    # the next tokens are 
    y = enc_sample[offset:context_size+offset]
    print(f"Taking a window of {context_size} tokens")
    print(f"x: {x}")
    print(f"With an offset of {offset} token(s)")
    print(f"y:      {y}")

    for i in range(1, context_size+1):
        context = enc_sample[:i]
        desired = enc_sample[i]
        print(context, "---->", desired)
        print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))


#========================================= GPTDatasetV1
class GPTDatasetV1(Dataset):
    '''
    This class create arrays of tensors for the input and the output
    The chunks have max_length length, and the stide can create overlapping
    '''
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []
        # all the text is tokenized
        token_ids = tokenizer.encode(txt)
        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + max_length + 1]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):
        return len(self.input_ids)
    
    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]

#========================================= create_dataloader
def create_dataloader_v1(txt, batch_size=4, max_length=256, stride=128, shuffle=True, drop_last=True, num_workers=0):
    '''
    This dataloader leverages the GPTDataset
    '''
    tokenizer = tiktoken.get_encoding("gpt2")
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,
        num_workers=num_workers
    )
    return dataloader


#========================================= test_dataloader
def test_dataloader():
    raw_text = ""
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    dataloader = create_dataloader_v1( raw_text, batch_size=1, max_length=4, stride=1, shuffle=False)
    data_iter = iter(dataloader)
    first_batch = next(data_iter)
    print(first_batch)
    second_batch = next(data_iter)
    print(second_batch)


#========================================= second_test_dataloader
def secondtest_dataloader():
    raw_text = ""
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    dataloader = create_dataloader_v1( raw_text, batch_size=8, max_length=4, stride=4, shuffle=False)
    data_iter = iter(dataloader)
    first_batch = next(data_iter)
    print(first_batch)

    
#========================================= embeddings_take1
def embeddings_take1():
    vocab_size = 6 # 50527 in GPT-3
    output_dim = 3 # 12288 in GPT-3
    torch.manual_seed(123)
    embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
    # creates a tensor with vocab_size lines (on per word) and output_dim columns
    print(embedding_layer.weight)
    print(embedding_layer(torch.tensor([3])))
    input_ids = torch.tensor([2, 3, 5, 1])
    print(embedding_layer(input_ids))

    

#+++++++++++++++++++++++++++++++++++++++++++++ main
def main():
    analyze_sample_file()
    first_usage_of_tokenizer()
    second_usage_of_tokenizer()
    test_dataloader()
    secondtest_dataloader()
    embeddings_take1()


    
if __name__ == "__main__":
    main()
