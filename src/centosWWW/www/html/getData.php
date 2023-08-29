<?php 

// 클라이언트로부터 전달받은 데이터를 json에 담아서 출력
$send["input1"]   =  $_POST['input1'];
$send["input2"]   =  $_POST['input2'];
$send["file"] =  $_FILES['fileInput'];
echo json_encode($send);
?>