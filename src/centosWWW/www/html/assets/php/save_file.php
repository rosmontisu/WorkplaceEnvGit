<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $userInput = $_POST["user_input"]; // 입력된 데이터 가져오기

    $fileName = "user_input.txt"; // 저장할 파일명
    $fileContent = $userInput . "\n"; // 데이터 줄바꿈 처리

    // 파일에 데이터 저장
    if (file_put_contents($fileName, $fileContent, FILE_APPEND | LOCK_EX) !== false) {
        echo "Data has been saved to the file.";
    } else {
        echo "Error saving data to the file.";
    }
}
?>
