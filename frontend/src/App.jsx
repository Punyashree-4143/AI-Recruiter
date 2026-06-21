import { useEffect, useState } from "react";
import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import Layout from "./components/Layout";
import CandidateDetailsPage from "./pages/CandidateDetailsPage";
import CandidateRankingPage from "./pages/CandidateRankingPage";
import DashboardPage from "./pages/DashboardPage";
import HiringDecisionPage from "./pages/HiringDecisionPage";
import JDAnalysisPage from "./pages/JDAnalysisPage";

const STORAGE_KEY = "ai-recruiter-result";

function loadStoredResult() {
  try {
    return JSON.parse(
      sessionStorage.getItem(STORAGE_KEY),
    );
  } catch {
    return null;
  }
}

export default function App() {
  const [result, setResult] = useState(
    loadStoredResult,
  );

  useEffect(() => {
    if (result) {
      sessionStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(result),
      );
    }
  }, [result]);

  const context = {
    result,
    setResult,
  };

  return (
    <Routes>
      <Route
        element={<Layout hasResult={Boolean(result)} />}
      >
        <Route
          path="/"
          element={
            <DashboardPage
              result={result}
              setResult={setResult}
            />
          }
        />
        <Route
          path="/jd-analysis"
          element={
            result ? (
              <JDAnalysisPage result={result} />
            ) : (
              <Navigate to="/" replace />
            )
          }
        />
        <Route
          path="/candidates"
          element={
            result ? (
              <CandidateRankingPage
                result={result}
              />
            ) : (
              <Navigate to="/" replace />
            )
          }
        />
        <Route
          path="/candidates/:candidateId"
          element={
            result ? (
              <CandidateDetailsPage
                result={result}
              />
            ) : (
              <Navigate to="/" replace />
            )
          }
        />
        <Route
          path="/decision"
          element={
            result ? (
              <HiringDecisionPage
                result={result}
              />
            ) : (
              <Navigate to="/" replace />
            )
          }
        />
        <Route
          path="*"
          element={<Navigate to="/" replace />}
        />
      </Route>
    </Routes>
  );
}
