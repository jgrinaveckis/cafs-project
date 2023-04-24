<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\LoginRequest;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function show() {
        return view('home');
    }

    public function login(LoginRequest $request) {

        $creds = request(['email', 'password']);
        #retireves jwt 
        $token = Auth::attempt($creds);
        
        if($token) {
            return response()->json([
                'access_token' => $token,
                'token_type' => 'bearer',
                'expires_in' => auth()->factory()->getTTL() * 60
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
