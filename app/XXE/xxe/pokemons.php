<!DOCTYPE html>
<html>
<head>
    <title>Enter XML Content</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Enter XML Content</h1>
        <form action="pokemon_response.php" method="post">
            <label for="xml_content">Enter XML Content:</label><br>
            <textarea name="xml_content" rows="6" cols="50"></textarea><br><br>
            <input type="submit" value="Submit XML Content">
        </form>
        
        <h2>Sample Input:</h2>
	<textarea name="xml_content" rows="8" cols="50">
<pokemon>
  <name>Pikachu</name>
  <type>Electric</type>
  <evolution>
      <stage>1</stage>
      <next>Raichu</next>
  </evolution>
</pokemon>
        </textarea>
    </div>
<p>P.S. Your flag is in the /flag1_dfg8va92j file</p>
</body>
</html>
