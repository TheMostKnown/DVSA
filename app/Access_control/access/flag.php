
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Access control</title>
    <link rel="stylesheet" href="static/style.css">
  </head>
  <body>
    <header>
    <div class="main-heading">
      <h1><span id="header">Your flag is <?php echo $_GET["flag"]; ?> !</span></h1>
    </div>  
    </header>

    <div class="margin-top-40">
        <button onclick="location.href='/'" type="button" class="button_index">Return</button>
    </div>


  </body>
</html>
