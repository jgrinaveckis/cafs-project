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
        Schema::create('lead_insert', function (Blueprint $table) {
            $table->id();
            $table->string('ip');
            $table->string('iso_state')->nullable();
            $table->string('iso_country')->nullable();
            $table->timestamp('lead_created_at')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('lead_insert');
    }
};
