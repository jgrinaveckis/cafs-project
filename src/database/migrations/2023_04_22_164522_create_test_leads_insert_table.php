<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('test_leads_insert', function (Blueprint $table) {
            $table->id();
            $table->string('ip');
            $table->string('iso_state');
            $table->string('iso_country');
            $table->decimal('lat', 8, 6);
            $table->decimal('lon', 9, 6);
            $table->timestamp('lead_created_at');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('test_leads_insert');
    }
};
