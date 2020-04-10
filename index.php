<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RUD</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="pic">
        <?php
            $command = escapeshellcmd('python getpic.py');
            $output = shell_exec($command);
            echo "<img src='$output'>";

            $output = substr($output, 10);
            $p = strpos($output, '_');
            $id =  substr($output, 0, $p);

            echo "<a href='https://vk.com/$id' target='_blank'><p>VK</p></a>";
        ?>
    </div>
    
</body>
</html>