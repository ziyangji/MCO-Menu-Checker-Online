<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends CommonController
{
    public function index()
    {
        $this->redirect('Index/home');
    }
    
    public function home()
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
                'name' => "Blitman Dining Hall",
                'addr' => "1800 6th Ave"
            ),
        );

        $this->assign('data', $dininghall);
        
        $this->display();
    }
    
    public function restaurant()
    {
        $res_name = I('get.name');
        
//        $data = shell_exec(escapeshellcmd('python3 '.$_SERVER['DOCUMENT_ROOT'].'/MCO-Menu-Checker-Online'.'/Public/assets/Python/data_fetch.py'));
//        
//        var_dump($data);
//        var_dump('python '.$_SERVER['DOCUMENT_ROOT'].'/MCO-Menu-Checker-Online'.'/Public/assets/Python/data_fetch.py');
        
        $this->assign('name', $res_name);
//        $this->assign('data', $data);
        $this->display();
    }
}