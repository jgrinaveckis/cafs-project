<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CalculatorController extends Controller
{
    public function calculate(string $type, int $first, int $second) {
        if ($type == "sum") {
            $sum = $first + $second;
            return $sum;
        }
        elseif ($type == "subtract") {
            $sum = $first - $second;
            return $sum;
        }
        elseif ($type == "multiply") {
            $sum = $first * $second;
            return $sum;
        }
        elseif ($type == "divide") {
            $sum = $first / $second;
            return $sum;
        }
        else {
            return "Please provide argument";
        }
    
    }
}
