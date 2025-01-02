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