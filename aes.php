<?php

function decryptAES($encryptedData, $key, $iv) {
    $cipher = "aes-256-cbc";
    $options = OPENSSL_RAW_DATA; // Specify RAW_DATA to avoid automatic base64 decoding

    $decryptedData = openssl_decrypt($encryptedData, $cipher, $key, $options, $iv);

    if ($decryptedData === false) {
        // Decryption failed
        echo "Error during decryption: " . openssl_error_string() . PHP_EOL;
        return false;
    }

    return $decryptedData;
}

// Read IVs from the file
$ivList = file("MyList.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

// Example usage:
$encryptedData = "XLVJNDGYUbaNXml6TOYlWTotgLv/PNP5Ar8fLl2t5PY="; // Replace with your actual encrypted data
$key = "php0p3nSsl3ncrypt10n"; // Replace with your 32-byte key

$decryptedData = null;

foreach ($ivList as $iv) {
    $decryptedData = decryptAES(base64_decode($encryptedData), $key, $iv);

    if ($decryptedData !== false) {
        echo $decryptedData . PHP_EOL; // Remove "Decrypted: " prefix
        // Continue trying other IVs
    }
}

if ($decryptedData === false) {
    echo "Decryption failed with all IVs." . PHP_EOL;
}

?>
