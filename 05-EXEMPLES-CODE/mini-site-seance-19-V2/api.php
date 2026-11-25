<?php
header('Content-Type: application/json; charset=utf-8');
echo json_encode([
    'success' => true,
    'message' => 'Réponse JSON produite par PHP côté serveur.',
    'session' => 19
], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
