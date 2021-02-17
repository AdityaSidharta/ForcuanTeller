import datetime
import json
import os
import subprocess

from forcuanteller.main.utils.paths import transform_dir, report_dir, template_path
import papermill as pm


def generate_reports(run_id):
    reports = []

    filename = "{}_{}.json".format("transform", run_id)
    filepath = os.path.join(transform_dir, filename)
    with open(filepath, "r") as f:
        report = json.load(f)

    buy_signals = report["buy_signals"]
    sell_signals = report["sell_signals"]

    reports.append(("md", "# Report for {}".format(datetime.datetime.now().strftime("%Y-%m-%d"))))

    if len(buy_signals):
        reports.append(("md", "## <span style='color:#60d24c'>Buy</span> signals"))
        for ticker, ticker_buy_signals in buy_signals.items():
            reports.append(("md", "### {}".format(ticker)))
            for indicator_buy_signal in ticker_buy_signals:
                date = indicator_buy_signal["datetime"]
                indicator = indicator_buy_signal["indicator"]
                param = indicator_buy_signal["param"]
                reason = indicator_buy_signal["reason"]
                image = indicator_buy_signal["image"]

                reports.append(("md", "#### {}".format(indicator)))
                reports.append(("md", "Date - {}".format(date)))
                reports.append(("md", "Parameters - {}".format(param)))
                reports.append(("md", "Reason - {}".format(reason)))
                reports.append(("image", image))

    if len(sell_signals):
        reports.append(("md", "## <span style='color:#d2544c'>Sell</span> signals"))
        for ticker, ticker_sell_signals in sell_signals.items():
            reports.append(("md", "### {}".format(ticker)))
            for indicator_sell_signal in ticker_sell_signals:
                date = indicator_sell_signal["datetime"]
                indicator = indicator_sell_signal["indicator"]
                param = indicator_sell_signal["param"]
                reason = indicator_sell_signal["reason"]
                image = indicator_sell_signal["image"]

                reports.append(("md", "#### {}".format(indicator)))
                reports.append(("md", "###### Date - {}".format(date)))
                reports.append(("md", "###### Parameters - {}".format(param)))
                reports.append(("md", "###### Reason - {}".format(reason)))
                reports.append(("image", image))

    return reports


def main(run_id):
    filename = "report_{}.ipynb".format(run_id)
    filepath = os.path.join(report_dir, filename)

    pm.execute_notebook(template_path, filepath, parameters={"run_id": run_id})
    subprocess.call(
        "jupyter nbconvert --to html --TemplateExporter.exclude_input=True {}".format(filepath), shell=True
    )
