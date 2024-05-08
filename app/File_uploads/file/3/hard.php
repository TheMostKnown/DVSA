<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> File uploaders team</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel=”stylesheet” href=”https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css” />
    <link rel="stylesheet" href="../static/style.css">

</head>
<?php
$output = "";
if (isset($_POST['actions'])) {
    $pwd = shell_exec('pwd');
    $parsed_value = str_replace(array('&', '|', '>', '<',' ', '/','..'), '', $_POST['actions'] );
    $command = "bash supersecretdir/" . $parsed_value;
    $output = shell_exec($command);
    if (str_contains($output, "sne{Its_1ike_pu22le}")){
        header("Location: ../flag.php?flag=sne{Its_1ike_pu22le}");
    }
}
?>
<body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <div class="container nav_bar">
        <div class="row">
            <div class="col-2 nav_logo"> <a href="/"></a> </div>
            <div class="col-10">
                <div class="nav_text"><a href="/">File uploaders team</a></div>
            </div>
        </div>
    </div>
    <header>
        <h1>Execute the best oneline bash code on this page!</h1>
    </header>
    <p></p>
    <p></p>
    <div class="output"><p>Output: <?php echo $output; ?></p></div>
    <p>There are best files what we choose which you can try to execute only on this page!</p>
    <form method="POST" class="login-page" action="hard.php" enctype="multipart/form-data" name="upload">
    <div class="grid-container">
       <button class="border-item" name="actions" value="flag.sh"> Read flag.txt </button>
        <button class="border-item" name="actions" value="firstusersfile.sh"> Th first user's file </button>
        <button class="border-item" name="actions" value="file1.sh"> Read file1.txt </button>
        <button class="border-item" name="actions" value="file2.sh"> Read file2.txt </button>
        <button class="border-item" name="actions" value="file3.sh"> Read file3.txt </button>
    </div>
    </form>
    <p></p>
    <p></p>
    <p>You can upload your version of best oneline code for our online tool and we will add it into our site. Maybe. </p>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2> Only text files! </h2>
            </div>
            <div class="col-12">
            <form method="POST" class="login-page" action="hard.php" enctype="multipart/form-data" name="upload">
                <input type="file" name="file" /><br>
                <p></p>
                <button type="submit" class="button_index" name="thebutton">Upload!</button>
            </form>
            </div>
        </div>
    </div>
</body>
</html>

<?php
if (isset($_POST['thebutton'])) {
    $path_parts = pathinfo($_FILES['file']['name']);
    if ($path_parts['extension'] == "txt") {
        if (move_uploaded_file($_FILES['file']['tmp_name'], "supersecretdir/" . basename($_FILES['file']['name']))){
            echo "Succsess!!!";
        }else{
            echo "Error";
        }
    }
}
?>