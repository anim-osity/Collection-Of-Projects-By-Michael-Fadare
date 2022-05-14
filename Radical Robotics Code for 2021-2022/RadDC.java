package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.OpMode; // this is where we import tools from other code
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.util.Range;
// import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.CRServo;
import com.qualcomm.robotcore.hardware.CRServoImplEx;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.CRServoImpl;


@TeleOp(name="RadDC", group="RadDC")

public class RadDC extends OpMode { // this is where we start the function
    private DcMotor FrontRight; // this is where we define the variables
    private DcMotor FrontLeft;
    private DcMotor BackRight;
    private DcMotor BackLeft;
    private DcMotor RightShooter; // this is where we define the variables
    private DcMotor LeftShooter;
    private DcMotor RightLoader;
    private DcMotor LeftLoader;
    private Servo LeftWobble;
    private Servo RightWobble;

    double fr; // defining variables part 2
    double fl;
    double br;
    double bl;
    double cl;
    double power;



    @Override
    public void init() {
        FrontRight = (DcMotor) hardwareMap.get("FrontRight"); // this is where we assign parts to variables
        FrontLeft = (DcMotor) hardwareMap.get("FrontLeft");
        BackRight = (DcMotor) hardwareMap.get("BackRight");
        BackLeft = (DcMotor) hardwareMap.get("BackLeft");
        RightShooter = (DcMotor) hardwareMap.get("RightShooter"); // this is where we assign parts to variables
        LeftShooter = (DcMotor) hardwareMap.get("LeftShooter");
        LeftLoader = (DcMotor) hardwareMap.get("LeftLoader");
        RightLoader = (DcMotor) hardwareMap.get("RightLoader");
        RightWobble = (Servo) hardwareMap.get("RightWobble");
        LeftWobble = (Servo) hardwareMap.get("LeftWobble");
        

        // FrontRight.setDirection(DcMotor.Direction.REVERSE); // this is where we set modes our code can execute in
        FrontLeft.setDirection(DcMotor.Direction.REVERSE);
        // BackRight.setDirection(DcMotor.Direction.REVERSE);
        BackLeft.setDirection(DcMotor.Direction.REVERSE);
        
        FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);

        
    }

    @Override
    public void init_loop() { // a bunch of logic when the code should execute
    }

    @Override
    public void start() { // a bunch of logic when the code should execute
    }


    @Override
    public void loop(){ 
        
        telemetry.addData("FrontLeft Encoder", FrontLeft.getCurrentPosition());

        
        if (gamepad1.dpad_left) {
            RightWobble.setPosition(.78);
            LeftWobble.setPosition(.17);
        }
        if(gamepad1.dpad_right){
            RightWobble.setPosition(.78);
            LeftWobble.setPosition(.17);
            
        }
        
        if (gamepad1.y) {
            LeftShooter.setPower(-1);
            RightShooter.setPower(0.7);
            
        }else{
            LeftShooter.setPower(0);
            RightShooter.setPower(0);
        }
    
        if (gamepad1.x) {
            LeftShooter.setPower(1);
            RightShooter.setPower(0.55);
        }
        else{
            LeftShooter.setPower(0);
            RightShooter.setPower(0);
        }
        
        if (gamepad1.a){
            LeftLoader.setPower(1);
            RightLoader.setPower(-1);
        }
        else{
            LeftLoader.setPower(0);
            RightLoader.setPower(0);
        }
        
        if (gamepad1.b){
            LeftLoader.setPower(-1);
            RightLoader.setPower(1);
        }
        else{
            LeftLoader.setPower(0);
            RightLoader.setPower(0);
        }
     
        
        if (gamepad1.left_bumper) {
            power = .25;
        } else {
            power = 1;
        }
    
        
       
        boolean slow = gamepad1.right_trigger > 0;
        double gamepad1LeftY = -gamepad1.left_stick_y; // * power; // assigns variables to inputs
        double gamepad1LeftX = -gamepad1.left_stick_x; // * power;
        double gamepad1RightX = -gamepad1.right_stick_x; // * power;

        double fl = (gamepad1LeftY + gamepad1LeftX - gamepad1RightX) / (slow ? 2 : 1); // controller logic nightmare scary
        double fr = (gamepad1LeftY - gamepad1LeftX + gamepad1RightX) / (slow ? 2 : 1); //back left
        double br = (gamepad1LeftY - gamepad1LeftX - gamepad1RightX) / (slow ? 2 : 1); //back right
        double bl = (gamepad1LeftY + gamepad1LeftX + gamepad1RightX) / (slow ? 2 : 1);

        FrontRight.setPower(Range.clip(fl, -0.96, 0.96)); // assigns power when inputs are triggered
        FrontLeft.setPower(Range.clip(fr, -1, 1));
        BackRight.setPower(Range.clip(br * 1, -0.96, 0.96));
        BackLeft.setPower(Range.clip(bl * .75, -1, 1));
        
    }
    
}
