<?php
/**
 * Created by PhpStorm.
 * User: Sun Yutao
 * Date: 2019/2/22
 * Time: 16:11
 */

class Database
{
    private $server; #"localhost" is fine
    private $username; #database username
    private $password; #password of username
    private $date;
    private $con;
    
    /** Database construction
        @param server The server's address, in form of ip:port
        @param username user's username in the server
        @param password user's password in the server
        @requires server, username, and password != null
     */
    function __construct($server, $username, $password)
    {
        $this->server = $server;
        $this->username = $username;
        $this->password = $password;
        $this->connect();
        $this->updateDate();

    }

    /** returns server's address
        @return server's address
     */
    public function server()
    {
        return $this->server;
    }

    /** returns today's date
     @return date
     */
    public function getDate()
    {
        return $this->date;
    }

    # also updates database
    public function updateDate()
    {
        #update date
        $this->date = date('Y_m_d');

        #create new database for new date
        $con = mysqli_connect($this->server, $this->username, $this->password);
        if(!$con)
        {
            throw new Exception('Connection Failed.');
        }

        $result = mysqli_query($con, "Create DATABASE {$this->date}");
        if(! $result)
        {
            throw new Exception("Error creating database: " . $con->error);
        }
        $con->close();

        #switch to new database
        $con = mysqli_connect($this->server, $this->username, $this->password, $this->date);
        if(!$con)
        {
            throw new Exception('Connection Failed.');
        }

        #create table for commons_breakfast
        $sql = "CREATE TABLE commons_breakfast(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for commons_lunch
        $sql = "CREATE TABLE commons_lunch(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for commons_dinner
        $sql = "CREATE TABLE commons_dinner(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for sage_breakfast
        $sql = "CREATE TABLE sage_breakfast(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for sage_lunch
        $sql = "CREATE TABLE sage_lunch(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for sage_dinner
        $sql = "CREATE TABLE sage_dinner(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for barh_breakfast
        $sql = "CREATE TABLE sage_breakfast(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for barh_lunch
        $sql = "CREATE TABLE sage_lunch(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        #create table for barh_dinner
        $sql = "CREATE TABLE sage_dinner(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, pic_name VARCHAR(30) NOT NULL, pic_addr VARCHAR(30) NOT NULL,)";
        if(!mysqli_query($con, $sql))
        {
            throw new Exception("Error creating table: " . mysqli_error($con));
        }

        $con->close();

    }

    /** returns whether the user is connect to its account
     @return server's address
     */
    public function connect()
    {
        #close the connection if there is one before
        if($this->con)
        {
            mysqli_close($this->con);
        }

        #reconnect to mysql
        $this->con = mysqli_connect($this->server, $this->username, $this->password);

        #throw exception if connection fails.
        if(!$this->connected()) {
            throw new Exception('Connection Failed.');
        }
    }

    private function connected()
    {
        if($this->con)
        {
            return false;
        }
        return true;
    }


    /** add a picture
     */
    public function addPic()
    {
        pass;
    }

    /** get a picture
     * return null if there is an error
     */
    public function getMenu($rest, $time, $today=true, $date=null)
    {

        if(!is_bool($today))
            #error
            #the input $today should be a boolean
            return null;

        ##update the required date
        if($today)
            $date = $this->date;

        if($date == null)
        {
            #error
            #date should not be empty when checking other days' menu
            return null;
        }

        #TODO: check date format

        #TODO: mysql statement

        ##TODO: get data from  database

        return null;
    }

}
