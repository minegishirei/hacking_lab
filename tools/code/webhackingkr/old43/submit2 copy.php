<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flag Viewer</title>
</head>
<body>
    <h1>Flag Viewer</h1>
    <div>
        <h2>Flag Content:</h2>
        <pre>
<?php
    // ファイルのパスを設定
    $flagFile = '/flag';

    // ファイルが存在し、読み取り可能であることを確認
    if (file_exists($flagFile) && is_readable($flagFile)) {
        // ファイルの内容を取得して表示
        echo htmlspecialchars(file_get_contents($flagFile));
    } else {
        // エラーメッセージを表示
        echo "The flag file is not accessible.";
    }
?>
        </pre>
    </div>
</body>
</html>