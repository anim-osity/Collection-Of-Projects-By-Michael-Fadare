package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.OpMode; // this is where we import tools from other code
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.util.Range;
import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.CRServo;
import com.qualcomm.robotcore.hardware.CRServoImplEx;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.CRServoImpl;
import com.qualcomm.robotcore.hardware.Servo;

@TeleOp(name="Fire", group="Fire")

public class Fire extends OpMode { // this is where we start the function
    private DcMotor RightShooter; // this is where we define the variables
    private DcMotor LeftShooter;
    private DcMotor RightLoader;
    private DcMotor LeftLoader;

    @Disabled
    @Override
    public void init() {
        RightShooter = (DcMotor) hardwareMap.get("RightShooter"); // this is where we assign parts to variables
        LeftShooter = (DcMotor) hardwareMap.get("LeftShooter");
        LeftLoader = (DcMotor) hardwareMap.get("LeftLoader");
        RightLoader = (DcMotor) hardwareMap.get("RightLoader");
        

    }

    @Override
    public void init_loop() { // a bunch of logic when the code should execute
    }

    @Override
    public void start() { // a bunch of logic when the code should execute
    }


    @Override
    public void loop(){ // a bunch of logic when the code should execute

        
        if (gamepad1.a) {
            LeftShooter.setPower(1);
            RightShooter.setPower(-1);
            
        }else{
            LeftShooter.setPower(0);
            RightShooter.setPower(0);
        }
    
        if (gamepad1.b) {
            LeftShooter.setPower(-1);
            RightShooter.setPower(1);
        }
        else{
            LeftShooter.setPower(0);
            RightShooter.setPower(0);
        }
        
        if (gamepad1.y){
            LeftLoader.setPower(-1);
            RightLoader.setPower(1);
        }
        else{
            LeftLoader.setPower(0);
            RightLoader.setPower(0);
        }
        
        if (gamepad1.x){
            LeftLoader.setPower(-1);
            RightLoader.setPower(1);
        }
        else{
            LeftLoader.setPower(0);
            RightLoader.setPower(0);
        }
        
        
        
        
     
        
    
    
        
       
       
    }
    
}
