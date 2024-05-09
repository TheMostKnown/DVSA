<?php
class User {
    public $name;
    public $role;
    public $role_hash;
    public $age;
    public $has_flag;

    public function __construct($name, $role, $role_hash, $age, $has_flag = false) {
        $this->name = $name;
        $this->role = $role;
        $this->role_hash = $role_hash;
        $this->age = $age;
        $this->has_flag = $has_flag;
    }
}

class Logger {
    private $event;
    private $callback;

    public function __construct($event) {
        $this->event = $event;
    }

    public function setCallback($callback) {
        if (is_callable($callback)) {
            $this->callback = $callback;
        }
    }

    public function log() {
        if (isset($this->callback)) {
            call_user_func($this->callback, $this->event);
        }
        return "[Event: {$this->event}]";
    }

    public function __wakeup() {
        if (isset($this->callback)) {
                $this->log();
        }
    }
}

$message = '';

$user = isset($_COOKIE['user']) ? unserialize(base64_decode($_COOKIE['user'])) : new User('User', 'Not Admin', '7ce36603ad38e9c4e0693bb4717213a0', 25);
if ($user->has_flag === true) {
    $message  .= 'Flag1: sne{g0thc4_th3_fl4g_1s_y0urs_ac4e0693bb} ';
}

if ($user->role == "Admin") {
    if ($user->role_hash == "supersecrethashyoushouldnotguessasdfvuixcvoijaweofhjasiduhvczxiu") { // If you are trying to solve the task from code, treat that you can't know the correct hash
        $message .= 'Flag2: sne{0k_1_b3l31ve_th4t_y0u_4r3_4dmin_201dc6546c}';
    } else {
        $message = 'Incorrect hash for Admin!!!';
    }
}

if (!isset($_COOKIE['user'])) {
    setcookie('user', base64_encode(serialize($user)), time() + 3600);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>User Serialization Service!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .container {
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Your personal data:</h1>
        <p><strong>Name:</strong> <?php echo $user->name; ?></p>
        <p><strong>Role:</strong> <?php echo $user->role; ?></p>
        <p><strong>Role Hash:</strong> <?php echo $user->role_hash; ?></p>
        <p><strong>Age:</strong> <?php echo $user->age; ?></p>
        <p><strong>Has Flag:</strong> <?php echo $user->has_flag ? 'Yes' : 'No'; ?></p>
        <p><strong>Message:</strong> <?php echo $message ?></p>
    </div>
</body>
</html>
