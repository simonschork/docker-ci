
<html>
    <head>
        <title>Weine</title>
    </head>

    <body>
        <h1>Weinauswahl</h1>
        <ul>
            <?php

            $json = file_get_contents('http://weine-service/');
            $obj = json_decode($json);

            $weine = $obj->weine;

            foreach ($weine as $wein) {
                echo "<li>$wein</li>";
            }
            ?>
        </ul>
    </body>
</html>