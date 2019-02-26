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

    function __construct($server, $username, $password)
    {
        $this->server = $server;
        $this->username = $username;
        $this->password = $password;

    }

    public function server()
    {
        return $this->server;
    }

    public function date()
    {
        return $this->date;
    }

    private function connect()
    {
        return true;
    }

    public function addPic()
    {
        pass;
    }

    public function getPic()
    {
        pass;
    }

}