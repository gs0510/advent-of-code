(* --Parsing-- *)
let read_file filename =
  let chan = open_in filename in
  let try_read () = try Some (input_line chan) with End_of_file -> None in
  let rec loop lines =
    match try_read () with
    | Some s -> loop (s :: lines)
    | None -> close_in chan ; List.rev lines
  in
  loop []

let parsed_input =
  read_file "input" |> List.map int_of_string

(* --puzzle1-- *)

let rec fuel_required l sum=
	match l with 
	| [] -> sum
	| h::t -> fuel_required t ( sum + h/3 - 2)
;;

let () = 
	Printf.printf "%d\n" (fuel_required parsed_input 0)
;;


(* --puzzle2-- *)

let rec helper value sum =
	if ((value/3) - 2)< 0 then sum
	else helper ((value/3) - 2) (sum + ((value/3) - 2))
;; 

let rec fuel_for_fuel l sum =
	match l with
	| [] -> sum
	| h::t -> fuel_for_fuel t (sum + (helper h 0))
;;

let () =
	Printf.printf "%d" (fuel_for_fuel parsed_input 0)
;;
