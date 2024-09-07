<?php
header('Content-Type: application/json');

// Connect to the database (update the credentials accordingly)
$host = 'localhost';
$dbname = 'cpc_leaderboard';
$user = 'cpc_cpc';
$password = 'TYEsZofXdR=Q';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Fetch users
    $usersQuery = $pdo->query("SELECT firstName, lastName, totalSolved, attendedMeetings, bonusProblems FROM users");
    $users = $usersQuery->fetchAll(PDO::FETCH_ASSOC);

    // Fetch sites
    $sitesQuery = $pdo->query("SELECT id, name FROM sites");
    $sites = $sitesQuery->fetchAll(PDO::FETCH_ASSOC);

    // Fetch tiers
    $tiersQuery = $pdo->query("SELECT name, minimumScore FROM tiers ORDER BY minimumScore DESC");
    $tiers = $tiersQuery->fetchAll(PDO::FETCH_ASSOC);

    // Prepare the response
    $response = [
        'users' => $users,
        'sites' => $sites,
        'tiers' => $tiers,
    ];

    // Output the response in JSON format
    echo json_encode($response);
} catch (PDOException $e) {
    // Handle any errors
    echo json_encode(['error' => $e->getMessage()]);
}
?>