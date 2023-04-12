<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\LogoutController;
use App\Http\Controllers\RegistrationController;
use App\Http\Controllers\LoginController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::group(['namespace' => 'App\Http\Controllers'], function () {

     Route::get('/', [HomeController::class, 'home'])->name('home');
    /**
     * Routes for authorized user
     */
     Route::group(['middleware' => ['auth']], function() {
        Route::get('/logout', [LogoutController::class, 'logout'])->name('logout');
    });

    /**
     * Routes for guest (un-auth) user
     */
    Route::group(['middleware' => ['guest']], function() {

        Route::get('/register', [RegistrationController::class, 'show'])->name('register_show');
        Route::post('/register', [RegistrationController::class, 'register'])->name('register');

        Route::get('/login', [LoginController::class, 'show'])->name('login_show');
        Route::post('/login', [LoginController::class, 'login'])->name('login');
    });
});