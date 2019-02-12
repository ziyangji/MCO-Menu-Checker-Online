<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends CommonController
{
    public function index()
    {
        $this->assign('content', '<div class="container"><h1>It works!</h1></div>');
        
//        menu template debug
        $this->redirect('Index/menu', 'loading menu...');

//        $this->display();
    }
    
    public function menu()
    {
        
        $dininghall = array(
            0 => array(
                'id' => 'cms',
                'name' => "Commons Dining Hall",
                'addr' => "TBD"
            ),
            1 => array(
                'id' => 'barh',
                
                'name' => "Barh Dining Hall",
                'addr' => "100 Albright Ct"
            ),
            2 => array(
                'id' => 'sage',
                'name' => "Sage Dining Hall",
                'addr' => "P8HC+WP"
            ),
            3 => array(
                'id' => 'blm',
                'name' => "Sage Dining Hall",
                'addr' => "1800 6th Ave"
            ),
        );

        $this->assign('data', $dininghall);
        
        $this->display();
    }
    
    public function restaurant()
    {
        $res_name = I('get.name');
        $this->assign('name', $res_name);
        $this->display();
    }
}