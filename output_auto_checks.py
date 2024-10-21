from auto_check_functions import *

def main():
    subdirectory = enterbox("Enter the output subdirectory path: ", "Locate Output to Check", "")
    context_file, input_file = detect_files(subdirectory)
    if not input_file:
        print("No input file found.")
        return

    context = read_context(context_file)
    result = validate_inputs(context, input_file)
    if result != "All checks passed":
        confirmation = ynbox(result, "Output Validity Warning")
        if confirmation == False:
            msgbox("Output Request Cancelled", "Output Validity Warning")
            return
        else:
            msgbox("Output Submitted. Note: Your output will be rejected if it violates the dislosure control rules. Please contact england.sde_service@nhs.net for more information", "Output Validity Warning")
    else:
        msgbox("Output Request Submitted", "Output Success Notification")

if __name__ == "__main__":
    main()
