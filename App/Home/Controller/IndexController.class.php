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
            'cms' => array(
                'id' => 0,
                'name' => "Commons Dining Hall",
                'addr' => "TBD"
            ),
            'barh' => array(
                'id' => 1,
                'name' => "Barh Dining Hall",
                'addr' => "100 Albright Ct"
            ),
            'sage' => array(
                'id' => 2,
                'name' => "Sage Dining Hall",
                'addr' => "P8HC+WP"
            ),
            'blm' => array(
                'id' => 3,
                'name' => "Sage Dining Hall",
                'addr' => "1800 6th Ave"
            ),
        );

        $this->assign('data', $dininghall);
        
        $this->display();
    }
}