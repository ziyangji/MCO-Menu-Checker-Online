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
    private $date;
    private $con;
    
    /** Database construction
        @param server The server's address
        @param username user's username in the server
        @param password user's password in the server
        @requires server, username, and password != null
     */
    function __construct($server, $username, $password)
    {
        $this->server = $server;
        $this->username = $username;
        $this->password = $password;

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
    public function date()
    {
        return $this->date;
    }

    /** returns whether the user is connect to its account
     @return server's address
     */
    private function connect()
    {
        return true;
    }

    /** add a picture
     */
    public function addPic()
    {
        pass;
    }

    /** get a picture
     */
    public function getPic()
    {
        pass;
    }

}
