<?php

namespace App\Http\Controllers;
use App\Models\TestLead;
use App\Models\Lead;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Gate;
use App\Http\Requests\LeadRequest;

class LeadController extends Controller 
{
    public function insert(LeadRequest $request) {
        $address = request('ip');

        if($address) {
            $lead = new TestLead();
            $lead->ip = $address;
            $lead->save();

            return response()->json([
                'message' => 'Succesful test IP address insert',
                ],
                200
            );
        }
        return response()->json([
            'message' => 'Error while trying to insert test ip',
            ],
            401
        );
    }

    public function getCountByCountry() {
        $leads = Lead::groupby('iso_country')
            ->select('iso_country', DB::raw('COUNT(*) AS count'))
            ->get();
        return $leads;
    }

    public function getCountByState() {
        $leads = Lead::groupby('iso_country','iso_state')
        ->select('iso_country','iso_state', DB::raw('COUNT(*) AS count'))
        ->get();
        return $leads;
    }
}