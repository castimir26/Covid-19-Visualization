describe("Form test", () => {
  it("Can fill the form", () => {
    cy.visit("/");
    cy.get("form");
  });
});
describe('The Home Page', function() {
  it('successfully loads', function() {
    cy.visit('http://localhost:8000') // change URL to match your dev URL
  });
});
