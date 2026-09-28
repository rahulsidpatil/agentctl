import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GovernanceArtifactsTest(unittest.TestCase):
    def test_required_project_artifacts_exist(self):
        expected = [
            "AGENTS.md",
            "CONTRIBUTING.md",
            "ROADMAP.md",
            "SECURITY.md",
            "SUPPORT.md",
            ".agentctl/config.json",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/dependabot.yml",
            "docs/backlog/mvp.md",
            "docs/history/project-origin.md",
            "docs/history/timeline.md",
            "docs/history/current-state.md",
            "docs/github-operations.md",
            "docs/decisions/ADR_TEMPLATE.md",
            "docs/experiments/EXPERIMENT_TEMPLATE.md",
            "docs/retrospectives/MILESTONE_RETROSPECTIVE_TEMPLATE.md",
            "docs/releases/RELEASE_REVIEW_TEMPLATE.md",
            "docs/sdlc/lifecycle.md",
            "docs/sdlc/tdd-policy.md",
            "docs/sdlc/metrics.md",
            "docs/sdlc/lessons.md",
        ]
        missing = [path for path in expected if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_agentctl_dogfood_configuration_is_portable(self):
        config = json.loads((ROOT / ".agentctl" / "config.json").read_text())
        self.assertEqual(1, config["schema_version"])
        self.assertEqual("agentctl", config["project"])
        self.assertEqual(["AGENTS.md"], config["instructions"])
        self.assertEqual(["codex", "claude", "antigravity"], config["providers"])
        serialized = json.dumps(config)
        self.assertNotIn(str(Path.home()), serialized)
        self.assertNotIn("/Users/", serialized)

    def test_issue_forms_cover_product_and_learning_work(self):
        template_root = ROOT / ".github" / "ISSUE_TEMPLATE"
        expected = {
            "bug.yml",
            "feature.yml",
            "platform-support.yml",
            "provider-integration.yml",
            "experiment.yml",
            "process-gap.yml",
        }
        self.assertTrue(expected.issubset({path.name for path in template_root.glob("*.yml")}))
        for filename in expected:
            text = (template_root / filename).read_text()
            self.assertIn("name:", text)
            self.assertIn("description:", text)
            self.assertIn("body:", text)

    def test_ci_keeps_old_checks_and_adds_cross_platform_gate(self):
        workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
        self.assertIn('python-version: ["3.9", "3.12"]', workflow)
        self.assertIn("ubuntu-latest", workflow)
        self.assertIn("macos-latest", workflow)
        self.assertIn("windows-latest", workflow)
        self.assertIn("name: required", workflow)
        self.assertIn("needs: [test, quality, platform-test, package]", workflow)


if __name__ == "__main__":
    unittest.main()
