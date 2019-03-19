<?php
/**
 * Created by PhpStorm.
 * User: Sun Yutao
 * Date: 2019/2/22
 * Time: 16:11
 */

class Database
{
    private $server;
    private $username;
    private $password;
    private $db_name;
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

    public function updateDate()
    {
        $this->date = date('Y-m-d');
    }

    /** returns whether the user is connect to its account
     @return server's address
     */
    private function connect()
    {
        #close the connection if there is one before
        if($this->con)
        {
            mysqli_close($this->con);
        }

        #reconnect to mysql
        $this->con = mysqli_connect($this->server, $this->username, $this->password);

        #throw exception if connection fails.
        if(!$this->checkConnection()) {
            throw new Exception('Connection Failed.');
        }
    }

    private function checkConnection()
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
