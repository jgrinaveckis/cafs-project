<?php

namespace App\Http\Controllers;

use App\Models\User;
use App\Http\Requests\RegistrationRequest;
use Illuminate\Support\Facades\Hash;

class RegistrationController extends Controller
{

    public function register(RegistrationRequest $request) {
        
        $email = $request->input('email');

        #Email is unique but take first() to return singular email
        $currUser = User::where('email', $email)->first();

        if ($currUser !== null) {
            return response(['error', 'Email is already taken'], 409);
        }

        $enteredPassword = $request->input('password');
        $hashedPassword = Hash::make($enteredPassword);

        $user = new User($request->all());
        $user->password = $hashedPassword;
        $user->save();

        return response(['success', 'User was registered succesfully'], 200);
    }
}
