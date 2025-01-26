package com.example.kokok;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

public class PasswordManager {

    public static String bytesToHex(byte[] bytes)
    {
        StringBuilder hexString = new StringBuilder();
        for (byte b: bytes)
        {
            String hex = Integer.toHexString(0xFF & b);
            if (hex.length() == 1)
            {
                hexString.append("0");
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }

    public static byte[] HexToBytes(String hex)
    {
        int len = hex.length();
        byte[] bytes = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            bytes[i / 2] = (byte) ((Character.digit(hex.charAt(i), 16) << 4)
                    + Character.digit(hex.charAt(i + 1), 16));
        }
        return bytes;
    }

    public static byte[] getSalt() throws NoSuchAlgorithmException
    {
        SecureRandom secureRandom = new SecureRandom();
        byte[] salt = new byte[16];
        secureRandom.nextBytes(salt);
        return salt;
    }

    public static String hashpassword(String password,byte[] salt) throws NoSuchAlgorithmException
    {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        digest.update(salt);
        byte[] hashedpassword = digest.digest(password.getBytes());
        return bytesToHex(hashedpassword);
    }

    public static boolean CheckPassword(String Check_Password , String Stored_Password , byte[] Stored_Salt) throws NoSuchAlgorithmException
    {
        String hashcheckpassword = hashpassword(Check_Password,Stored_Salt);
        return hashcheckpassword.equals(Stored_Password);
    }
}
