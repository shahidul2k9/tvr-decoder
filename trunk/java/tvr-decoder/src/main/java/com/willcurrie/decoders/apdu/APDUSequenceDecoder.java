package com.willcurrie.decoders.apdu;

import com.willcurrie.DecodedData;
import com.willcurrie.Decoder;

import java.util.ArrayList;
import java.util.List;

public class APDUSequenceDecoder implements Decoder {

    private ReplyAPDUDecoder replyDecoder;
    private CommandAPDUDecoder[] commandDecoders;

    public APDUSequenceDecoder(ReplyAPDUDecoder replyDecoder, CommandAPDUDecoder... commandDecoders) {
        this.replyDecoder = replyDecoder;
        this.commandDecoders = commandDecoders;
    }

    @Override
    public List<DecodedData> decode(String input, int startIndexInBytes) {
        DecodeSession session = new DecodeSession();
        ArrayList<DecodedData> list = new ArrayList<DecodedData>();
        for (String line : input.split(" ")) {
            CommandAPDUDecoder commandDecoder = getCommandDecoder(line);
            DecodedData decoded;
            if (commandDecoder != null) {
                decoded = commandDecoder.decode(line, startIndexInBytes, session);
            } else {
                decoded = replyDecoder.decode(line, startIndexInBytes, session);
            }
            list.add(decoded);
            startIndexInBytes = decoded.getEndIndex();
        }
        return list;
    }

    private CommandAPDUDecoder getCommandDecoder(String input) {
        APDUCommand command = APDUCommand.fromHex(input.substring(0, 4));
        for (CommandAPDUDecoder commandDecoder : commandDecoders) {
            if (commandDecoder.getCommand() == command) {
                return commandDecoder;
            }
        }
        return null;
    }

    @Override
    public String validate(String input) {
        return null;
    }

    @Override
    public int getMaxLength() {
        return Integer.MAX_VALUE;
    }
}