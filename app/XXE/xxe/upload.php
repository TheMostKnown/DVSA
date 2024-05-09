<?php
if(isset($_POST["submit"])) {
    libxml_disable_entity_loader(false); // Enable external entities
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
    $allowed_formats = ["image/svg+xml", "image/jpeg", "image/png"];
    
    $file_type = mime_content_type($_FILES["fileToUpload"]["tmp_name"]);
    
    // MIME Type check
    if (!in_array($file_type, $allowed_formats)) {
        echo "Mime Type Conflict.";
        $uploadOk = 0;
    }

    
    // Check file size
    if ($_FILES["fileToUpload"]["size"] > 500000) {
        echo "Sorry, your file is too large.";
        $uploadOk = 0;
    }
    
    // Allow only certain file formats
    $allowed_types = array('png', 'jpeg', 'svg');
    if(!in_array($imageFileType, $allowed_types)) {
        echo "Sorry, only PNG, JPEG, and SVG files are allowed.";
        $uploadOk = 0;
    }
    
    // Check if $uploadOk is set to 0 by an error
    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    // if everything is ok, try to upload file
    } else {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
            echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
            // Show image contents to the user
            $file_contents = file_get_contents($target_file);
            if ($file_type === "image/svg+xml") {
                $dom = new DOMDocument();
                $dom->loadXML($file_contents, LIBXML_NOENT | LIBXML_DTDLOAD);
                $doc = simplexml_import_dom($dom);
                $xxe_result = $doc->text;
                echo "<br><br>SVG Text Section:<br><pre>" . htmlspecialchars($xxe_result) . "</pre>";
            }
            echo "<br><br>Contents:<br><pre>" . htmlspecialchars($file_contents) . "</pre>";
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }
}
?>
