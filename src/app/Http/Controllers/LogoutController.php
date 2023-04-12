<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Session;

class LogoutController extends Controller
{
    public function logout(Request $request)
    {
        //logout and flush all session info via Facade
        Auth::logout();
        Session::flush();
        
        return redirect('login');
    }
}
