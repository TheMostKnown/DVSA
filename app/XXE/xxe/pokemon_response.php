<?php
libxml_disable_entity_loader(false); // Enable external entities

$xml_content = isset($_POST['xml_content']) ? $_POST['xml_content'] : '';

if (!empty($xml_content)) {
    $doc = new DOMDocument();
    $doc->loadXML($xml_content, LIBXML_NOENT | LIBXML_DTDLOAD); // Vulnerable to XXE

    $pokemon_name = $doc->getElementsByTagName('name')->item(0)->nodeValue;
    $pokemon_type = $doc->getElementsByTagName('type')->item(0)->nodeValue;

    echo "Pokemon Name: " . $pokemon_name . "<br>";
    echo "Pokemon Type: " . $pokemon_type . "<br>";

    // Potentially more processing based on the XML content
} else {
    echo "No XML content provided.";
}
?>
