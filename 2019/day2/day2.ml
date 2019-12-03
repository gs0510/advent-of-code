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
	Array.of_list (read_file "input" |> List.hd |> String.split_on_char ',' |> List.map int_of_string)
;;

(* --puzzle1-- *)

exception Foo of string

let execute arr index =
	Printf.printf "%d\n" index ;
	let operand1, operand2 = arr.(arr.(index+1)), arr.(arr.(index+2)) in
	let dest = arr.(index+3) in
	match arr.(index) with
	| 1 -> arr.(dest) <- operand1 + operand2
	| 2 -> arr.(dest) <- operand1 * operand2
	| _ -> ()
;;

let rec gravity_assist arr index=
	match arr.(index) with
	| 1 | 2 -> execute arr index; gravity_assist arr (index+4)
	| _ ->  arr.(0)
;; 

let setup val1 val2=
	let arr = Array.copy parsed_input in
	arr.(1) <- val1;
	arr.(2) <- val2;
	arr
;;	

let () = 
	Printf.printf "%d\n" (gravity_assist (setup 12 2) 0)
;;

(* --puzzle2-- *)

let rec find_inputs noun verb =
	Printf.printf "%d %d\n" noun verb;
	let output = gravity_assist (setup noun verb) 0 in
	match output with
	| 19690720 -> (100*noun + verb)
	| _ -> 
		if verb <= 99 then (find_inputs noun (verb+1))
		else if noun <= 99  then (find_inputs (noun+1) 0)
		else raise(Foo "no combination!")
;;

let () =
	Printf.printf "%d\n" (find_inputs 0 0)
;;
