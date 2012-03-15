package com.willcurrie.decoders;

public enum APDUCommand {
    Select("00A4"),
    ReadRecord("00B2"),
    GetProcessingOptions("80A8"),
    GenerateAC("80AE"),
    ComputeCryptographicChecksum("802A");

    private String firstTwoBytes;

    private APDUCommand(String firstTwoBytes) {
        this.firstTwoBytes = firstTwoBytes;
    }

    public String getFirstTwoBytes() {
        return firstTwoBytes;
    }

    public static APDUCommand fromHex(String hex) {
        APDUCommand[] values = values();
        for (APDUCommand value : values) {
            if (value.getFirstTwoBytes().equals(hex)) {
                return value;
            }
        }
        return null;
    }
}