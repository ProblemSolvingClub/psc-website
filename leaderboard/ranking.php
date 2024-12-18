<?php
header('Content-Type: application/json');

error_reporting(E_ALL);
ini_set('display_errors', 1);

// Connect to the database (update the credentials accordingly)
$host = 'localhost';
$dbname = 'cpc_leaderboard';
$user = 'cpc_cpc';
$password = 'yWXvO{$ZSG,?';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    try {
        $usersQuery = $pdo->query("SELECT firstName, lastName, totalSolved, attendedMeetings, bonusProblems FROM users");
        $users = $usersQuery->fetchAll(PDO::FETCH_ASSOC);
        if (!$users) {
            throw new Exception("Query returned no rows.");
        }
    } catch (PDOException $e) {
        echo "PDO Error: " . $e->getMessage();
    } catch (Exception $e) {
        echo "General Error: " . $e->getMessage();
    }

    // Fetch users
    $usersQuery = $pdo->query("SELECT firstName, lastName, totalSolved, attendedMeetings, bonusProblems FROM users");
    $users = $usersQuery->fetchAll(PDO::FETCH_ASSOC);

    // Fetch sites
    $sitesQuery = $pdo->query("SELECT id, name FROM sites");
    $sites = $sitesQuery->fetchAll(PDO::FETCH_ASSOC);

    // Fetch tiers
    $tiersQuery = $pdo->query("SELECT name, minimumScore FROM tiers ORDER BY minimumScore ASC");
    $tiers = $tiersQuery->fetchAll(PDO::FETCH_ASSOC);

    // Prepare the response
    $response = [
        'users' => $users,
    ];

    // Output the response in JSON format
    echo json_encode($response);
} catch (PDOException $e) {
    // Handle any errors
    echo json_encode(['error' => $e->getMessage()]);
}
?>