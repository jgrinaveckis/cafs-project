<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\LoginRequest;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function login(LoginRequest $request) {

        $creds = request(['email', 'password']);
        $token = Auth::attempt($creds);
        
        if($token) {
            return response()->json([
                'token' => $token
            ]);
        } else {
            return response()->json([
                'message' => 'Invalid credentials. Email or password is incorrect.',
                'errors' => []
                ],
                401
            );
        }
    }
}
