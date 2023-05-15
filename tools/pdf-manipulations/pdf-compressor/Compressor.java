package com;

import java.io.*;
import com.itextpdf.text.*;
import com.itextpdf.text.pdf.*;

public class Compressor {
    public static void compressPdf(String src, String dest) throws IOException, DocumentException {
        PdfReader reader = new PdfReader(src);
        PdfStamper stamper = new PdfStamper(reader, new FileOutputStream(dest), PdfWriter.VERSION_1_5);
        stamper.getWriter().setCompressionLevel(9);
        int total = reader.getNumberOfPages() + 1;
        for (int i = 1; i < total; i++) {
            reader.setPageContent(i, reader.getPageContent(i));
        }
        stamper.setFullCompression();
        stamper.close();
        reader.close();
    }
    public static void main(String args[]) {
        try {
            int len = args.length;
            System.out.println("Length of arguments: " + len);
            if (len >= 1) {
                Compressor.compressPdf(args[0],"output.pdf");
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}



