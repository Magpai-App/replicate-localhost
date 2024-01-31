import os
import subprocess
import threading
import uuid
import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

JOBS = {}


def run_command(cmd, id):
    global JOBS
    try:
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        stdout, stderr = process.communicate()

        JOBS[id].update(
            {
                "status": "succeeded",
                "output": stdout.decode(),
                "logs": stderr.decode(),
                "error": "",
                "completed_at": datetime.datetime.now().isoformat(),
            }
        )
    except Exception as e:
        JOBS[id] = {"status": "failed", "error": str(e)}
    print(JOBS)


@app.route("/v1/predictions", methods=["POST"])
def predictions():
    global JOBS

    # Generate random id
    ID = str(uuid.uuid4())

    data = request.json

    version = data.get(
        "version"
    )  # For now, this is the full image name needed for cog, not just the version... See readme
    inputs = data.get("input")

    print(
        """Running prediction on model version: [{}]. With inputs: [{}]""".format(
            version, inputs
        )
    )

    # Ensure docker is running
    # TODO

    # If windows, ensure wsl is
    # TODO

    # Build commands

    # Format inputs into command string

    inputArgs = ""

    for key, value in inputs.items():
        # @TODO: We don't know here if the input is a file or a string... Files need an @ prefix...
        inputArgs += " -i {}='{}'".format(key, value)

    CMD = """cog predict {} {}""".format(version, inputArgs)


    if os.name == "nt":
        CMD = "wsl " + CMD

    print(" - cmd: {}".format(CMD))
    
    threading.Thread(target=run_command, args=(CMD, ID)).start()

    jobData = {
        "id": ID,
        "status": "starting",
        "result": None,
        "error": None,
        "version": "",
        "created_at": datetime.datetime.now().isoformat(),
        "started_at": datetime.datetime.now().isoformat(),
    }

    JOBS[ID] = jobData

    return jobData


@app.route("/v1/predictions/<string:ID>", methods=["GET"])
def get_predictions(ID):
    global JOBS

    process_info = JOBS.get(ID)

    if process_info is None:
        return jsonify({"error": "Invalid ID"}), 404

    return jsonify(process_info)
