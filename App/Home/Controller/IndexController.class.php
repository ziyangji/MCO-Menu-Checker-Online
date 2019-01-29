<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends CommonController
{
    public function index()
    {
        $this->assign('content', '<div class="container"><h1>It works!</h1></div>');
        $this->display();
    }
    
    public function menu()
    {
        $this->display();
    }
}