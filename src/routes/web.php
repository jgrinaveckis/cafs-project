<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\LogoutController;
use App\Http\Controllers\MapController;
use App\Http\Controllers\RegistrationController;
use App\Http\Controllers\ConsumerController;

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

    Route::get('/', [LoginController::class, 'show'])->name('login_show');
    Route::post('/', [LoginController::class, 'login'])->name('login');
    Route::get('/register', [RegistrationController::class, 'show'])->name('register_show');
    Route::post('/register', [RegistrationController::class, 'register'])->name('register');

    /**
     * Routes for authorized user
     */
     Route::group(['middleware' => ['auth']], function() {
        Route::get('/map', [MapController::class, 'show'])->name('map');
        Route::get('/logout', [LogoutController::class, 'logout'])->name('logout');
        Route::get('/aggregations', [AggregationsController::class, 'show'])->name('aggregations');
    });

});