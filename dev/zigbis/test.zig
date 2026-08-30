const std = @import("std");
const builtin = @import("builtin");

const expect = std.testing.expect;
const expectEqual = std.testing.expectEqual;
const print = std.debug.print;
const warn = std.log.warn;

pub fn main() void {
    print("Hello, {s}!\n", .{"World"});
}


test "always succeeds" {
    try expect(true);
}

//test "always fails" {
//    try expect(false);
//}

test "if statement expression" {
    const a = true;
    var x: u16 = 0;
    x += if (a) 1 else 2;
    try expect(x == 1);
}

test "while loop continue expression" {
    var i: usize = 0;
    while (i < 10) : (i += 1) {
        //warn("{}", .{i});
        print("{}\n", .{i}); // do not forget the \n
    }
    try expectEqual(10, i);
}

test "while with continue expression" {
    const test_name = @src().fn_name;
    print("Test name: {s}\n", .{test_name});

    var sum: u8 = 0;
    var i: u8 = 1;
    while (i <= 10) : (i += 1) {
        sum += i;
        print("{}\n", .{sum});
    }
    try expect(sum == 55);
}
