scenario "Nilai Mata Kuliah" {
  given
    tugas = 80;
    kuis  = 70;
    uts   = 75;
    uas   = 85;
  calculate
    nilai_akhir = 0.2 * tugas + 0.2 * kuis + 0.25 * uts + 0.35 * uas;
    if nilai_akhir >= 85 then
      grade = "A";
    else if nilai_akhir >= 70 then
      grade = "B";
    else if nilai_akhir >= 55 then
      grade = "C";
    else
      grade = "D";
    end
  report
    nilai_akhir as "Nilai akhir";
    grade as "Grade huruf";
}

scenario "Simple Beam" {
  given
    w = 10;   // kN/m
    L = 5;    // m
  calculate
    reaction = w * L / 2;
    shear_max = reaction;
  report
    reaction as "Reaction (kN)";
    shear_max as "Max shear (kN)";
}