#!C:/Python311/python.exe
print("content-type: text/html \r\n\r\n")

print('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    
    <title>Admin Dashboard</title>
    
    <style>
        body {
            font-family: Roboto Mono,
            margin: 0;
            padding: 0;
        }

        .navbar {
            margin-bottom: 0;
            background-color: #3d424f;
        }

        .navbar-brand,
        .navbar-nav>li>a {
            color: rgb(123, 111, 129);
        }

        .navbar-brand:hover,
        .navbar-nav>li>a:hover {
            color: #18bc9c;
        }

        .sidebar {
            height: 100%;
            width: 250px;
            background-color: #42304a;
            position: fixed;
            top: 51px;
            left: 0;
            padding-top: 20px;
            transition: all 0.3s ease;
            z-index: 1000;
            overflow-y: auto;
        }

        .sidebar a {
            padding: 10px 15px;
            text-decoration: none;
            font-size: 18px;
            color: white;
            display: block;
        }

        .sidebar a:hover {
            background-color: #4d4e4e;
            color: white;
        }

        .main-content {
            margin-left: 250px;
            padding: 20px;
            transition: margin-left 0.3s ease;
        }

        @media (max-width: 768px) {
            .sidebar {
                position: fixed;
                top: 51px;
                left: -250px;
                width: 250px;
                transition: left 0.3s ease;
            }

            .sidebar.in {
                left: 0;
            }

            .main-content {
                margin-left: 0;
            }
        }

        @media (max-width: 480px) {
            .sidebar a {
                text-align: center;
                font-size: 16px;
            }
        }
    </style>
</head>

<body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#sidebar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Admin Dashboard</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#"><span class="glyphicon glyphicon-user"></span> Profile</a></li>
                    <li><a href="#"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="sidebar collapse" id="sidebar">
        <a href="#"><span class="glyphicon glyphicon-user"></span> Profile</a>
        <a href="#dashboard"><i class="fa fa-dashboard"></i> Dashboard</a>
        <a href="#users"><i class="fa fa-users"></i> Users</a>
        <a href="#reports"><i class="fa fa-bar-chart"></i> Reports</a>
        <a href="#settings"><i class="fa fa-cogs"></i> Settings</a>
        <a href="#"><span class="glyphicon glyphicon-log-out"></span> Logout</a>
    </div>
    <div class="sidebar ">
        <a href="#"><span class="glyphicon glyphicon-user"></span> Profile</a>
        <a href="#dashboard"><i class="fa fa-dashboard"></i> Dashboard</a>
        <a href="#users"><i class="fa fa-users"></i> Users</a>
     
        <a href="#reports"><i class="fa fa-bar-chart"></i> Reports</a>
        <a href="#settings"><i class="fa fa-cogs"></i> Settings</a>
    </div>

    <div class="main-content" style="padding-top: 60px;">
        <h2 class="text-center">Welcome to the Admin Dashboard</h2>
      
    </div>


</body>

</html>
''')