<?php

namespace App\Http\Controllers;
use App\Models\Lead;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Gate;

class LeadController extends Controller 
{
    public function getCountByCountry() {
        $leads = Lead::groupby('iso_country')
            ->select('iso_country', DB::raw('COUNT(*) AS count'))
            ->get();
            return $leads;
    }

    public function getCountByState() {
        $leads = Lead::groupby('iso_state')
        ->select('iso_state', DB::raw('COUNT(*) AS count'))
        ->get();
        return $leads;
    }
}